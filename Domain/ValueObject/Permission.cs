using System.ComponentModel.DataAnnotations;

namespace AlfaCoreDumped.Domain.ValueObject
{
    public class Permission
    {
        [Key]
        public Guid Id { get; set; }

        [Required]
        public string PermissionName { get; set; }
    }
}
